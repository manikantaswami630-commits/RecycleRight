import sentry_sdk
sentry_sdk.init(dsn="https://9550064fe8dec4a9342263a760dd68f5@o4512168812871680.ingest.us.sentry.io/4512191643975680")
raise Exception("Sentry test")