from typing import List, Dict, Optional

from pydantic import BaseModel, Field


class Config(BaseModel):
    model_config = {"extra": "forbid"}


class ModuleConfig(Config):
    """
    Configuration for a single module within a project.
    """

    tags: List[str]
    strict: bool = False

    @classmethod
    def from_yml(cls, content: str) -> "ModuleConfig":
        # TODO: Mocking for now
        return cls(tags=["test"], strict=False)


class ScopeDependencyRules(Config):
    """
    Dependency rules for a particular scope.
    """

    depends_on: List[str]


class ProjectConfig(Config):
    """
    Configuration applied globally to a project.
    """

    constraints: Dict[str, ScopeDependencyRules]
    ignore: Optional[List[str]] = Field(default_factory=list)
