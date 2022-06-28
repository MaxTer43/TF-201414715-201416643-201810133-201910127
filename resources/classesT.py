class Street:
  _id = any 
  _name = any
  _Qinter = any
  def __init__(self, id, name, Qinter):
    self._id = id
    self._name = name
    self._Qinter = Qinter

class Intersection:
  _idRegistry = any 
  _idStreet = any
  _nameStreet = any
  _idOrAndDest = (any, any)
  _OrAndDest = (any, any)
  _disKm = any
  _velKmh = any
  _price = any
  _revertPrice = any
  _interCoord1 = (any, any)
  _interCoord2 = (any, any)
  def __init__(self, idRegistry, idStreet, nameStreet, idOrigin, idestination, OrAndDest1, OrAndDest2, disKm, velKmh, price, revertPrice, interCoord11, interCoord12,interCoord21,interCoord22):
    self._idRegistry = idRegistry 
    self._idStreet = idStreet
    self._nameStreet = nameStreet
    self._idOrAndDest = (idOrigin, idestination)
    self._OrAndDest = (OrAndDest1, OrAndDest2)
    self._disKm = disKm
    self._velKmh = velKmh
    self._price = price
    self._revertPrice = revertPrice
    self._interCoord1 = (interCoord11, interCoord12)
    self._interCoord2 = (interCoord21, interCoord22)