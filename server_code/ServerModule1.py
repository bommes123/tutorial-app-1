import anvil.server

# Aufruf der Pi-Funktion
print(anvil.server.call('hallo', 'Dietmar'))  # => "Hallo Dietmar vom Raspberry Pi!"
print(anvil.server.call('addiere', 5, 7))     # => 12

# Wenn LED-Funktionen aktiviert
# anvil.server.call('led_an')
# anvil.server.call('led_aus')

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
#@anvil.server.callable
#def get_model():
#  return "Some model number"

