import configparser
from common.basedir import BASEDIR

default_config_file_path = '%s/../tinkla_openpilot.cfg' % BASEDIR

class ConfigFile():
  config_file_r = 'r'
  config_file_w = 'w'

  ### Do NOT modify here, modify in /data/tinkla_openpilot.cfg and reboot
  def read(self, into, config_path):
      configr = configparser.RawConfigParser()
      file_changed = False

      try:
        configr.read(config_path)
        fd = open(config_path, "r")
        prev_file_contents = fd.read()
        fd.close()
      except IOError:
        prev_file_contents = ""
        print("no config file, creating with defaults...")

      radar_section = 'RADAR_CONFIG'
      config = configparser.RawConfigParser(allow_no_value=True)
      config.add_section(radar_section)

      #radar_vin -> into.radarVIN
      default_radar_vin = '"                 "'
      into.radarVIN, didUpdate = self.read_config_entry(
        config, configr, prev_file_contents, section = radar_section,
        entry = 'radar_vin', entry_type = str,
        default_value = default_radar_vin,
        comment = 'If you use an aftermarket Tesla Bosch Radar that already has a coded VIN, you will have to enter that VIN value here.'
      )
      file_changed |= didUpdate
      
      if into.radarVIN == '':
        into.radarVIN = default_radar_vin
        file_changed = True

      #radar_offset -> radarOffset
      into.radarOffset, didUpdate = self.read_config_entry(
        config, configr, prev_file_contents, section = radar_section,
        entry = 'radar_offset', entry_type = float,
        default_value = 0,
        comment = 'If your Tesla Bosch Radar is not centered on the car, this value will allow to enter a correction offset.'
      )
      file_changed |= didUpdate

      #radar_epas_type -> radarEpasType
      into.radarEpasType, didUpdate = self.read_config_entry(
        config, configr, prev_file_contents, section = radar_section,
        entry = 'radar_epas_type', entry_type = int,
        default_value = 0,
        comment = 'Depending on the source of your Tesla Bosch Radar (older or newer Model S or Model X), ' + 
              'this setting has to match what the radar was programmed to recognize as EPAS; values are between 0 and 4; finding the right one is trial and error.'
      )
      file_changed |= didUpdate

      #radar_position -> radarPosition
      into.radarPosition, didUpdate = self.read_config_entry(
        config, configr, prev_file_contents, section = radar_section,
        entry = 'radar_position', entry_type = int,
        default_value = 0,
        comment = 'Depending on the source of your Tesla Bosch Radar (older or newer Model S or Model X), ' + 
               'this setting has to match what the radar was programmed to have a position (Model S, Model S facelift, Model X); values are between 0 and 3; finding the right one is trial and error.'
      )
      file_changed |= didUpdate

      if file_changed:
        did_write = True
        with open(config_path, self.config_file_w) as configfile:
          config.write(configfile)
      else:
        did_write = False

      # Remove double quotes from VIN (they are required for empty case)
      into.radarVIN = into.radarVIN.replace('"', '')
      return did_write

  def read_config_entry(self, config, configr, prev_file_contents, section, entry, entry_type, default_value, comment):
      updated = self.update_comment(config, prev_file_contents, section, entry, default_value, comment)
      result = None
      try:
        if entry_type == bool:
          result = configr.getboolean(section, entry)
        elif entry_type == int:
          result = configr.getint(section, entry)
        elif entry_type == float:
          result = configr.getfloat(section, entry)
        else:
          result = configr.get(section, entry)
      except (configparser.NoSectionError, configparser.NoOptionError):
        result = default_value
        updated = True
      config.set(section, entry, result)
      return result, updated

  def update_comment(self, config, prev_file_contents, section, entry, default_value, comment):
      new_comment = ("# " + entry + ": " + comment + " (Default: " + str(default_value) + ")").lower()
      config.set(section, new_comment)
      updated = (prev_file_contents.find(new_comment) == -1)
      return updated

class CarSettings():
  radarVIN = None
  radarOffset = None
  radarEpasType = None
  radarPosition = None

  def __init__(self, optional_config_file_path = default_config_file_path):
    config_file = ConfigFile()
    self.did_write_file = config_file.read(self, config_path = optional_config_file_path)

  def get_value(self, name_of_variable):
    return self.__dict__[name_of_variable]

# Legacy support
def read_config_file(into, config_path = default_config_file_path):
  config_file = ConfigFile()
  config_file.read(into, config_path)