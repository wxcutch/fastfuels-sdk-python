# coding: utf-8

"""
    FastFuels API

    A JSON API for creating, editing, and retrieving 3D fuels data for next generation fire behavior models.

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from fastfuels_sdk.client_library.models.export_status import ExportStatus
from typing import Optional, Set
from typing_extensions import Self

class Export(BaseModel):
    """
    Request to export a resource
    """ # noqa: E501
    domain_id: Optional[StrictStr] = Field(default=None, alias="domainId")
    resource: Optional[StrictStr] = None
    sub_resource: Optional[StrictStr] = Field(default=None, alias="subResource")
    attribute: Optional[StrictStr] = None
    format: Optional[StrictStr] = None
    status: Optional[ExportStatus] = None
    created_on: Optional[datetime] = Field(default=None, alias="createdOn")
    modified_on: Optional[datetime] = Field(default=None, alias="modifiedOn")
    signed_url: Optional[StrictStr] = Field(default=None, alias="signedUrl")
    expires_on: Optional[datetime] = Field(default=None, alias="expiresOn")
    __properties: ClassVar[List[str]] = ["domainId", "resource", "subResource", "attribute", "format", "status", "createdOn", "modifiedOn", "signedUrl", "expiresOn"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Export from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if domain_id (nullable) is None
        # and model_fields_set contains the field
        if self.domain_id is None and "domain_id" in self.model_fields_set:
            _dict['domainId'] = None

        # set to None if resource (nullable) is None
        # and model_fields_set contains the field
        if self.resource is None and "resource" in self.model_fields_set:
            _dict['resource'] = None

        # set to None if sub_resource (nullable) is None
        # and model_fields_set contains the field
        if self.sub_resource is None and "sub_resource" in self.model_fields_set:
            _dict['subResource'] = None

        # set to None if attribute (nullable) is None
        # and model_fields_set contains the field
        if self.attribute is None and "attribute" in self.model_fields_set:
            _dict['attribute'] = None

        # set to None if format (nullable) is None
        # and model_fields_set contains the field
        if self.format is None and "format" in self.model_fields_set:
            _dict['format'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if created_on (nullable) is None
        # and model_fields_set contains the field
        if self.created_on is None and "created_on" in self.model_fields_set:
            _dict['createdOn'] = None

        # set to None if modified_on (nullable) is None
        # and model_fields_set contains the field
        if self.modified_on is None and "modified_on" in self.model_fields_set:
            _dict['modifiedOn'] = None

        # set to None if signed_url (nullable) is None
        # and model_fields_set contains the field
        if self.signed_url is None and "signed_url" in self.model_fields_set:
            _dict['signedUrl'] = None

        # set to None if expires_on (nullable) is None
        # and model_fields_set contains the field
        if self.expires_on is None and "expires_on" in self.model_fields_set:
            _dict['expiresOn'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Export from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domainId": obj.get("domainId"),
            "resource": obj.get("resource"),
            "subResource": obj.get("subResource"),
            "attribute": obj.get("attribute"),
            "format": obj.get("format"),
            "status": obj.get("status"),
            "createdOn": obj.get("createdOn"),
            "modifiedOn": obj.get("modifiedOn"),
            "signedUrl": obj.get("signedUrl"),
            "expiresOn": obj.get("expiresOn")
        })
        return _obj


