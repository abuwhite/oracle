from rdoclient import RandomOrgClient
import settings

api = RandomOrgClient(settings.API)

print(api.generate_integers(1, 0, 3))