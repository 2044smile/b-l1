from django.db import models


# 회사의 코드를 사용
# 사용할 필요가 없어보임
# class BaseModel(models.Model):
#
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         blank=True,
#         null=False,
#         verbose_name="생성 일시",
#         help_text="데이터가 생성된 날짜입니다.",
#     )
#     updated_at = models.DateTimeField(
#         auto_now=True,
#         blank=True,
#         null=False,
#         verbose_name="수정 일시",
#         help_text="데이터가 수정된 날짜입니다.",
#     )


class Vietnam(models.Model):
    area = models.CharField(max_length=30)
    description = models.CharField(max_length=100, blank=True, null=True)
    temperature = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.area}의 정보"
