import component

conversionsMass = { "g":1, "lb": 453.592, "kg":1000}
conversionsVolume = {"ml":1, "cup":236.588, "gal":3785.41, "L":1000 }

def convertMass(amount, source, to) -> float:
    convertFactor = conversionsMass[source]/conversionsMass[to]
    convert = amount *convertFactor
    return convert
def convertVolume(amount, source, to) -> float:
    convertFactor = conversionsVolume[source]/conversionsVolume[to]
    convert = amount * convertFactor
    return convert
def convertUnified(amount, source, to, ingrd: component.ingredient.Ingredient ) -> float:
    ### If source volume, get in ml, find in g
    if source in conversionsVolume:
        sourceStandardVolume = convertVolume(amount, source, "ml")
        ## density defined as g/ml
        sourceStandardMass = ingrd.density * sourceStandardVolume
    ### Convert to standard g
    elif source in conversionsMass:
        sourceStandardMass = convertMass(amount, source, "g")
    ### Find destination
    ### If we are looking for a volume, convert to ml, then convert to target
    if to in conversionsVolume:
        toStandardVolume = sourceStandardMass / ingrd.density
        convertedAmount = convertVolume(toStandardVolume, "ml", to)
    ### If we are looking for a mass, convert to mass
    elif to in conversionsMass:
        convertedAmount = convertMass(sourceStandardMass, "g", to)
    return convertedAmount

