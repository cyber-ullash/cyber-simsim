from fastapi import FastAPI, Request, Response
import httpx

app = FastAPI()

ULLASH_API = "আব্বু ডাক ENDPOINT দিবো"  #হেইটারসদের আম্মু কে গন*ধর্ষ√ণ করি\∆ ধন্যবাদ 🫰🏾 🫶🏾 

@app.api_route("/{path:path}", methods=["GET", "POST"])
async def mask_api(path: str, request: Request):
    async with httpx.AsyncClient() as client:
        upstream_url = f"{ULLASH_API}/{path}"

██╗░░░██╗██╗░░░░░██╗░░░░░░█████╗░░██████╗██╗░░██╗
██║░░░██║██║░░░░░██║░░░░░██╔══██╗██╔════╝██║░░██║
██║░░░██║██║░░░░░██║░░░░░███████║╚█████╗░███████║।        Ullash ッ
██║░░░██║██║░░░░░██║░░░░░██╔══██║░╚═══██╗██╔══██║
╚██████╔╝███████╗███████╗██║░░██║██████╔╝██║░░██║

        
        # Forward headers except host, user-agent for minimal trace
        headers = {k: v for k, v in request.headers.items() if k.lower() not in ["host", "user-agent"]}
        method = request.method
        params = dict(request.query_params)
        data = await request.body()

        # Send request upstream
        upstream_response = await client.request(
            method,
            upstream_url,
            headers=headers,
            params=params,
            content=data,
            timeout=20.0
        )

        return Response(
            content=upstream_response.content,
            status_code=upstream_response.status_code,
            media_type=upstream_response.headers.get("content-type")
        )
██╗░░░██╗██╗░░░░░██╗░░░░░░█████╗░░██████╗██╗░░██╗
██║░░░██║██║░░░░░██║░░░░░██╔══██╗██╔════╝██║░░██║
██║░░░██║██║░░░░░██║░░░░░███████║╚█████╗░███████║
██║░░░██║██║░░░░░██║░░░░░██╔══██║░╚═══██╗██╔══██║
╚██████╔╝███████╗███████╗██║░░██║██████╔╝██║░░██║
