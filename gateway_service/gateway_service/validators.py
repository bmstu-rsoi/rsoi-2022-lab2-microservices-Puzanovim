from gateway_service.exceptions import ValidationError


def validate_page_size_params(page: int, size: int) -> None:
    if not 0 <= page:
        raise ValidationError('Page should not be less then 0')
    if not 1 <= size <= 100:
        raise ValidationError('Size should be between 1 and 100')
