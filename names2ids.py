def name2id(name, outformat):

  import cirpy
  import chemspipy
  import queryDevice  
  
  idstring = None
  source = None

  if idstring is None:
    source = 'NCI'
    idstring = cirpy.resolve(name, outformat)
  if idstring is None:
    source = 'ChemSpi'
    chemspid = chemspipy.find_one(name)
    try:
      smiles = chemspid.smiles
      idstring = cirpy.resolve(smiles, outformat)
    except AttributeError:
      idstring = None
  if idstring is None:
    source = 'NCI-pattern-match'
    idstring = cirpy.resolve(name, outformat,['name_pattern'])
  if idstring is None:
    source = None
    idstring = str(idstring)
  try: 
    idstring = (idstring.rstrip(),source)
  except AttributeError:
    idstring  = (idstring[0].rstrip(),source)
    print 'There were multiple results for: ', name, ' using: ', idstring[0], '\n', idstring 

  return idstring
