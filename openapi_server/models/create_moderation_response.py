# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401
from openapi_server.models.create_moderation_response_results_inner import CreateModerationResponseResultsInner


class CreateModerationResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    CreateModerationResponse - a model defined in OpenAPI

        id: The id of this CreateModerationResponse.
        model: The model of this CreateModerationResponse.
        results: The results of this CreateModerationResponse.
    """

    id: str = Field(alias="id")
    model: str = Field(alias="model")
    results: List[CreateModerationResponseResultsInner] = Field(alias="results")

CreateModerationResponse.update_forward_refs()