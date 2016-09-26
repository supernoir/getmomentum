def momentum():
    print "=== === ===\nGET MOMENTUM\n=== === ==="
    mass = input("Please supply given mass (in kg) ")
    print "--- --- ---"
    velocity = input ("Please supply given velocity change (in m/s) ")
    print "--- --- ---"
    momentum = mass * velocity
    print "Momentum would be " + str(momentum) + " kg-m/s"
    print "=== === ==="
    return;

momentum()