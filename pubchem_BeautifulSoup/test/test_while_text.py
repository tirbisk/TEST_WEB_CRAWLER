ret = ''

shesh = ''
shesh = 'P210, P233, P240, P241, P242, P243, P261, P264, P271, P280, P303+P361+P353, P304+P340, P305+P351+P338, P312, P337+P313, P370+P378, P403+P233, P403+P235, P405, and P501, P210, P233, P240, P241, P242, P243, P261, P264, P271, P280, P303+P361+P353, P304+P340, P305+P351+P338, P312, P337+P313, P370+P378, P403+P233, P403+P235, P405, and P501, P201, P202, P210, P233, P240, P241, P242, P243, P260, P261, P264, P271, P280, P281, P301+P310, P303+P361+P353, P304+P340, P305+P351+P338, P308+P313, P312, P314, P331, P337+P313, P370+P378, P403+P233, P403+P235, P405, and P501'
shish =  'P210, P233, P240, P241, P242, P243, P261, P264, P271, P280, P303+P361+P353, P304+P340, P305+P351+P338, P312, P337+P313, P370+P378, P403+P233, P403+P235, P405, and P501'
shash = 'P201, P202, P210, P233, P240, P241, P242, P243, P260, P261, P264, P271, P280, P281, P301+P310, P303+P361+P353, P304+P340, P305+P351+P338, P308+P313, P312, P314, P331, P337+P313, P370+P378, P403+P233, P403+P235, P405, and P501'

shysh = shesh.split()
shysh = list(dict.fromkeys(shysh))
print(''.join(shysh))