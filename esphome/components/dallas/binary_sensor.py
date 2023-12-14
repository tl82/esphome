import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import (
  CONF_ADDRESS,
  CONF_DALLAS_ID,
  CONF_INDEX,
  DEVICE_CLASS_PRESENCE,
)
from . import DallasComponent, dallas_ns

iButtonBinarySensor = dallas_ns.class_("iButtonBinarySensor", binary_sensor.BinarySensor)

CONFIG_SCHEMA = cv.All(
  binary_sensor.binary_sensor_schema(
    iButtonBinarySensor,
    device_class=DEVICE_CLASS_PRESENCE,
  ).extend(
    {
      cv.GenerateID(CONF_DALLAS_ID): cv.use_id(DallasComponent),
      cv.Required(CONF_ADDRESS): cv.hex_uint64_t,
    }
  ),
)


async def to_code(config):
  hub = await cg.get_variable(config[CONF_DALLAS_ID])
  var = await binary_sensor.new_binary_sensor(config)

  cg.add(var.set_address(config[CONF_ADDRESS]))

  cg.add(var.set_parent(hub))

  cg.add(hub.register_ibutton(var))
