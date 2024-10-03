from http import HTTPStatus
from typing import Dict, List

from fastapi import APIRouter, HTTPException, Path, Query

from ..service.account_service import AccountService
from ..service.price_plan_service import PricePlanService
from .electricity_reading_controller import repository as readings_repository
from .models import OPENAPI_EXAMPLES, PricePlan, PricePlanPeakTimeMultipliers, PricePlanComparisons

service = PricePlanService(readings_repository)


router = APIRouter(
    prefix="/price-plans",
    tags=["Price Plans Peak Controller"],
)


@router.post(
    "/peak/store",
    description="Store Price Plan Peak Time Multipliers",
)
def store(data: PricePlanPeakTimeMultipliers):
    return service.store_peak_multipliers(data.pricePlanId, data.model_dump(mode="json"))


@router.post(
    "/peak/clear-all",
    description="Store Price Plan Peak Time Multipliers",
)
def store(data: PricePlan):
    return service.clear_all_peak_multipliers(data.pricePlanId)
