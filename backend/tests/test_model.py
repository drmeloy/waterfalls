from django.test import TestCase
from ..models import Waterfall

class WaterfallTest(TestCase):
  def setUp(self):
    Waterfall.objects.create(
      name='Super Falls', height='555 ft.', longitude='123 N', latitude='321 W', description='Super cool falls'
    )
    Waterfall.objects.create(
      name='Lame Falls', height='7 ft.', longitude='987 S', latitude='789 E', description='Pretty lame falls'
    )

  def test_waterfall(self):
    super_falls = Waterfall.objects.get(name='Super Falls')
    lame_falls = Waterfall.objects.get(name='Lame Falls')
    self.assertEqual(
      super_falls.describe_waterfall(), 'Super Falls is 555 ft. tall and is located at 123 N and 321 W.'
    )
    self.assertEqual(
      lame_falls.describe_waterfall(), 'Lame Falls is 7 ft. tall and is located at 987 S and 789 E.'
    )
    