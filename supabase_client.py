from dotenv import load_dotenv
load_dotenv()
import os
# import supabase
from supabase import create_client , AuthInvalidCredentialsError



from supabase_client import create_client
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
# print(supabase)

# data = supabase.table("users").select("id").execute()
# print(data)

data = supabase.table("projects").insert({"username":"Nathan", "email":"nathan@example.com","clerk_id":"2"}).execute()
print(data)

