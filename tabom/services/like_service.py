# 단위 테스트
from tabom.models import Like


def do_like(user_id: int, article_id: int) -> Like:
    return Like.objects.create(user_id=user_id, article_id=article_id)


def undo_like(user_id: int, article_id: int) -> tuple[int, dict[str, int]]:
    return Like.objects.filter(user_id=user_id, article_id=article_id).delete()
