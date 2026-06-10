from roenpilot.common.numpy_fast import clip


def rate_limit_numpy_fast(new_value, last_value, dw_step, up_step):
  return clip(new_value, last_value + dw_step, last_value + up_step)
