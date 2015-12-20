from . jedi_completion import JediCompletionProvider
from . word_completion import WordCompletionProvider
from . operator_completion import OperatorCompletionProvider
from . static_pattern_completion import StaticPatternProvider
from ... settings import get_preferences

jedi_provider = JediCompletionProvider()
word_provider = WordCompletionProvider()
operator_provider = OperatorCompletionProvider()
static_pattern_provider = StaticPatternProvider()

def complete(text_block):
    setting = get_preferences().completion_providers

    completions = []
    completions.extend(static_pattern_provider.complete(text_block))
    if setting.use_operator_completion: completions.extend(operator_provider.complete(text_block))
    if setting.use_jedi_completion: completions.extend(jedi_provider.complete(text_block))
    if setting.use_word_completion: completions.extend(word_provider.complete(text_block))

    primary, secondary = [], []
    for c in completions:
        if c.type == "PARAMETER": primary.append(c)
        else: secondary.append(c)

    return primary + secondary
