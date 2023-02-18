import pynecone as pc

config = pc.Config(
    app_name="Chemistry hmm",
    api_url="https://beppvis.github.io/chemistry-praticlas",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
