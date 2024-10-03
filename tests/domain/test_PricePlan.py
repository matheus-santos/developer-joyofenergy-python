from datetime import datetime
from unittest import TestCase

from src.domain.price_plan import PricePlan


class TestPricePlan(TestCase):
    def test_return_the_base_price_given_an_off_peak_date_time(self):
        peak_time_multiplier = PricePlan.PeakTimeMultiplier(PricePlan.DayOfWeek.WEDNESDAY, 10)
        off_peak_time = datetime(2000, 1, 1, 11, 11, 11)

        plan = PricePlan("plan-name", "supplier-name", 1, [peak_time_multiplier])

        price = plan.get_price(off_peak_time)

        self.assertEqual(price, 1)

    def test_return_a_peak_price_given_a_datetime_matching_peak_day(self):
        peak_time_multiplier = PricePlan.PeakTimeMultiplier(PricePlan.DayOfWeek.WEDNESDAY, 10)
        off_peak_time = datetime(2000, 1, 5, 11, 11, 11)

        plan = PricePlan("plan-name", "supplier-name", 1, [peak_time_multiplier])

        price = plan.get_price(off_peak_time)

        self.assertEqual(price, 10)

    def test_change_multiplier_by_index(self):
        # Arrange
        peak_time_multiplier = PricePlan.PeakTimeMultiplier(PricePlan.DayOfWeek.WEDNESDAY, 10)
        plan = PricePlan("plan-name", "supplier-name", 1, [peak_time_multiplier])

        # Act
        plan.change_multiplier_by_index(0, 255)

        # Assert
        self.assertEqual(plan.peak_time_multipliers[0].multiplier, 255)

    def test_should_not_change_multiplier_when_index_not_exist(self):
        # Arrange
        peak_time_multiplier = PricePlan.PeakTimeMultiplier(PricePlan.DayOfWeek.WEDNESDAY, 10)
        plan = PricePlan("plan-name", "supplier-name", 1, [peak_time_multiplier])

        # Act
        plan.change_multiplier_by_index(1, 255)  # Index is off

        # Assert
        self.assertEqual(len(plan.peak_time_multipliers), 1)
        self.assertEqual(plan.peak_time_multipliers[0].multiplier, 10)

    def test_should_add_multiplier(self):
        plan = PricePlan("plan-name", "supplier-name", 1, [])

        plan.add_multiplier(PricePlan.DayOfWeek.WEDNESDAY, 2)
        plan.add_multiplier(PricePlan.DayOfWeek.WEDNESDAY, 2.5)

        self.assertEqual(len(plan.peak_time_multipliers), 2)
        self.assertEqual(plan.peak_time_multipliers[0].multiplier, 2)
        self.assertEqual(plan.peak_time_multipliers[1].multiplier, 2.5)
