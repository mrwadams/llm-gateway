from litellm.integrations.custom_guardrail import CustomGuardrail
import re

BLOCKED_PATTERNS = [
    # Violence / weapons
    r"\b(how to (make|build|create) (a )?(bomb|weapon|explosive|gun|knife))\b",
    r"\b(how to (kill|hurt|harm|injure|murder))\b",
    r"\b(suicide|self[- ]harm)\b",
    # Drugs
    r"\b(how to (make|cook|synthesize|grow) (meth|cocaine|heroin|drugs|lsd))\b",
    # Adult content
    r"\b(porn|pornograph|nsfw|xxx|hentai)\b",
    r"\b(sexting)\b",
    # Dangerous activities
    r"\b(how to hack|how to steal|how to break into)\b",
    # Jailbreak attempts
    r"\b(ignore (previous |your |all )?instructions)\b",
    r"\b(you are now|pretend (to be|you are)|jailbreak|DAN mode)\b",
    r"\b(ignore (the |your )?system prompt)\b",
]


class ChildSafetyGuardrail(CustomGuardrail):
    """Blocks dangerous or inappropriate queries before they reach the LLM."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def async_pre_call_hook(self, user_api_key_dict, cache, data, call_type):
        messages = data.get("messages", [])
        for message in messages:
            content = message.get("content", "")
            if isinstance(content, str):
                self._check_content(content)

    def _check_content(self, text: str):
        text_lower = text.lower()
        for pattern in BLOCKED_PATTERNS:
            if re.search(pattern, text_lower):
                raise Exception(
                    "This request was blocked by the content filter. "
                    "If you think this is a mistake, ask a parent for help."
                )
