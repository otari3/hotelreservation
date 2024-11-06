class DataBaseErrors:
  class DataBaseExeption(Exception):
    pass
  class FormatingError(DataBaseExeption):
    pass
  class ExecuteQuery(DataBaseExeption):
    pass
  class SelectOneError(DataBaseExeption):
    pass
  class SelectAll(DataBaseExeption):
    pass
  class AddinRoomsError(DataBaseExeption):
    pass
  class UpdatingRoomsError(DataBaseExeption):
    pass