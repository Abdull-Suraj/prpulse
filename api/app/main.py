from fastapi import FastAPI

app = FastAPI(title='PRPulse')


@app.get('/health')
async def health():
    return {'status': 'ok'}