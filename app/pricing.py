# Safe division
def safe_divide(numerator, denominator, default=0):
    if denominator == 0:
        logger.warning('Division by zero prevented, returning default')
        return default
    return numerator / denominator