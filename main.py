import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration

sentry_sdk.init(
    dsn="https://9550064fe8dec4a9342263a760dd68f5@o4512168812871680.ingest.us.sentry.io/4512191643975680",
    integrations=[FastApiIntegration()],
    traces_sample_rate=1.0,   # captures performance traces
    send_default_pii=True,    # includes user info in errors
)