def make_spread(strike, bid, ask):
    return {'strikePrice': strike, 'bid': bid, 'ask': ask}

# Taken from the SNAP option chain on 2/22/2020 lol
TEST_STRIKEMAP_NEAR = {12: {'CALL': make_spread(12, 4.7, 4.8),
                       'PUT': make_spread(12, 0.02, 0.03)},
                  13: {'CALL': make_spread(13, 3.7, 3.8),
                       'PUT': make_spread(13, 0.04, 0.05)},
                  14: {'CALL': make_spread(14, 2.79, 2.84),
                       'PUT': make_spread(14, 0.09, 0.1)},
                  15: {'CALL': make_spread(15, 1.92, 1.96),
                       'PUT': make_spread(15, 0.22, 0.23)},
                  16: {'CALL': make_spread(16, 1.18, 1.23),
                       'PUT': make_spread(16, 0.48, 0.5)},
                  17: {'CALL': make_spread(17, 0.66, 0.68),
                       'PUT': make_spread(17, 0.94, 0.96)},
                  18: {'CALL': make_spread(18, 0.33, 0.34),
                       'PUT': make_spread(18, 1.6, 1.63)},
                  19: {'CALL': make_spread(19, 0.15, 0.17),
                       'PUT': make_spread(19, 2.42, 2.46)},
                  20: {'CALL': make_spread(20, 0.07, 0.08),
                       'PUT': make_spread(20, 3.3, 3.4)},
                  21: {'CALL': make_spread(21, 0.03, 0.04),
                       'PUT': make_spread(21, 4.3, 4.35)}
                  }

TEST_STRIKEMAP_FAR = {12: {'CALL': make_spread(12, 4.75, 4.85),
                       'PUT': make_spread(12, 0.05, 0.07)},
                  13: {'CALL': make_spread(13, 3.8, 3.9),
                       'PUT': make_spread(13, 0.12, 0.13)},
                  14: {'CALL': make_spread(14, 2.96, 3),
                       'PUT': make_spread(14, 0.24, 0.25)},
                  15: {'CALL': make_spread(15, 2.18, 2.21),
                       'PUT': make_spread(15, 0.45, 0.47)},
                  16: {'CALL': make_spread(16, 1.52, 1.56),
                       'PUT': make_spread(16, 0.79, 0.81)},
                  17: {'CALL': make_spread(17, 1, 1.04),
                       'PUT': make_spread(17, 1.27, 1.29)},
                  18: {'CALL': make_spread(18, 0.64, 0.66),
                       'PUT': make_spread(18, 1.9, 1.93)},
                  19: {'CALL': make_spread(19, 0.39, 0.41),
                       'PUT': make_spread(19, 2.65, 2.68)},
                  20: {'CALL': make_spread(20, 0.24, 0.26),
                       'PUT': make_spread(20, 3.45, 3.55)},
                  21: {'CALL': make_spread(21, 0.15, 0.16),
                       'PUT': make_spread(21, 4.35, 4.45)}
                  }
