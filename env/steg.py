import http.client, urllib.request, urllib.parse, urllib.error, base64
import re
import json

async def ocr(ctx, args, key, endpoint):
    """
        reads an image and convert it to a text (OCR)
        usage: 
        z-ocr help
        z-ocr [lang (id, en, etc)] [image attachment]    
    """
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key,
    }
    lang = args[0]
    imageUrl = ctx.message.attachments[0].url
    endpointDomain = re.search('https?://([A-Za-z_0-9.-]+).*', endpoint).group(1)
    params = urllib.parse.urlencode({
        # Request parameters
        'language': lang,
        'detectOrientation': 'true',
        'model-version': 'latest',
    })

    try:
        conn = http.client.HTTPSConnection(endpointDomain)
        conn.request("POST", "/vision/v3.2/ocr?%s" % params, "{\"url\":\"%s\"}" % imageUrl, headers)
        response = conn.getresponse()
        data = response.read()
        data_str = data.decode('utf-8')
        json_str = json.dumps(data_str)
        d = json.loads(json_str)
        printstr = ""
        for line in d["regions"][0]["lines"]:
            for word in line["words"]:
                printstr += word["text"]
            printstr += "\n"

        await ctx.send(printstr)
        conn.close()
    except Exception as e:
        await ctx.send(e)
        await ctx.send("[Errno {0}] {1}".format(e.errno, e.strerror))