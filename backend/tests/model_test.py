from django.test import TestCase
from .models import Waterfall

# Test for Waterfall model
class WaterfallTest(TestCase):
  def setUp(self):
    Waterfall.objects.create(
      name='Super Falls', height='555 ft.', longitude='123 N', latitude='321 W', description='Super cool falls'
    )
    Waterfall.objects.create(
      name='Lame Falls', height='7 ft.', longitude='987 S', latitude='789 E', description='Pretty lame falls'
    )

  def test_waterfall