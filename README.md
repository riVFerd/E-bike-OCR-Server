# Flask OCR KTM API

### Request Parameter
| Parameter | Type          | Description |
|-----------|---------------| --- |
| `image`   | `Image Files` | **Required**. Image file to be processed. |

### Success Response
Json Response was set by `KTMModel` class model in `ktm_model.py`.  
Example success json response:
```json
{
    "nim": "2141000000",
    "nama": "FULL NAME",
    "ttl": "CityName, January 22, 2005",
    "jurusan": "D-IV T. INFORMATIKA",
    "alamat": "Slope Street No. 46"
}
```