from typing import TYPE_CHECKING, Callable

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from account.domain.models.manager import UserManager
from patient_management.core.models import ModelsBase

if TYPE_CHECKING:
    from account.domain.models.profile import EmployeProfile  # noqa: TCH004


class User(AbstractBaseUser, ModelsBase):  # type: ignore[misc]
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        verbose_name="username",
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={"unique": "A user with that username already exists."},
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. "
        "Unselect this instead of deleting accounts.",
    )

    USERNAME_FIELD = "username"

    objects = UserManager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    @property
    def profile(self) -> "EmployeProfile":
        return self.profile

    @property
    def is_staff(self) -> bool:
        return self.profile.is_superuser  # type: ignore

    @property
    def has_module_perms(self) -> Callable[..., bool]:
        return self.profile.has_module_perms

    @property
    def has_perm(self) -> Callable[..., bool]:
        return self.profile.has_perm
