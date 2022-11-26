from gateway_service.apis.rating_system_api.schemas import UserRating


async def smth():
    pass


class RatingSystemAPI:
    async def get_rating(self, name: str) -> UserRating:
        user_rating: UserRating = await smth()
        return user_rating
