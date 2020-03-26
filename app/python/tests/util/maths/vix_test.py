import unittest

from util.maths.vix import smallest_difference, T, F, K_0, merge_k0, get_otm_options, sigma_squared
from .vix_data import TEST_STRIKEMAP_NEAR, TEST_STRIKEMAP_FAR


class TestVIX(unittest.TestCase):
    def test_smallest_difference(self):
        smallest_diff = smallest_difference(TEST_STRIKEMAP_NEAR)
        self.assertDictEqual(smallest_diff, {'strike': 17, 'call_price': 0.67, 'put_price': 0.95})

# TODO:
#     def test_T(self):
#          pass
    def test_F(self):
        f = F(strike=17, r=0.02, t=0.05, call_price=0.67, put_price=0.95)
        self.assertAlmostEqual(f, 16.7197199)

    def test_K_0(self):
        k_0 = K_0(16.7197199, TEST_STRIKEMAP_NEAR)
        self.assertEqual(k_0, 16)

    def test_merge_k0(self):
        k0_entry = merge_k0(16, TEST_STRIKEMAP_NEAR)
        self.assertDictEqual(k0_entry, {'bid': 0.83, 'ask': 0.865, 'strikePrice': 16})

    def test_get_otm_options(self):
        # Calls
        otm_calls = get_otm_options(k_0=16, contract_type='CALL', strikemap=TEST_STRIKEMAP_NEAR)
        self.assertEqual(otm_calls, [option['CALL'] for strike, option in TEST_STRIKEMAP_NEAR.items() if strike > 16])
        
        # Puts
        otm_puts = get_otm_options(k_0=16, contract_type='PUT', strikemap=TEST_STRIKEMAP_NEAR)
        self.assertEqual(otm_puts, [option['PUT'] for strike, option in TEST_STRIKEMAP_NEAR.items() if strike < 16])

    def test_sigma_squared(self):
        otm_options =  get_otm_options(16, 'PUT', TEST_STRIKEMAP_NEAR) + [merge_k0(16, TEST_STRIKEMAP_NEAR)] + get_otm_options(16, 'CALL', TEST_STRIKEMAP_NEAR)
        sig_sq = sigma_squared(t=0.05, r=0.02, f=16.7197199, k_0=16, K_i=otm_options)
        self.assertAlmostEqual(sig_sq, 0.331803277)

if __name__ == '__main__':
    unittest.main()