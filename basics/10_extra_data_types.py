# Extra Data Types
# Learn to use advanced Python data types with FastAPI

from datetime import datetime, time, timedelta
from typing import Annotated, Union
from uuid import UUID
from fastapi import Body, FastAPI

app = FastAPI()

# TODO: Create the read_items endpoint
# Endpoint: PUT /items/{item_id}
# Parameters:
# - item_id: UUID (path parameter)
# - start_datetime: Annotated[datetime, Body()]
# - end_datetime: Annotated[datetime, Body()]
# - process_after: Annotated[timedelta, Body()]
# - repeat_at: Annotated[Union[time, None], Body()] = None
#
# Inside the function:
# - Calculate start_process = start_datetime + process_after
# - Calculate duration = end_datetime - start_process
# - Return a dict keyed by the parameter names, plus the two calculated values:
#   {"item_id": ..., "start_datetime": ..., "end_datetime": ...,
#    "process_after": ..., "repeat_at": ..., "start_process": ...,
#    "duration": ...}

@app.put("/items/{item_id}")
async def create_item(item_id: UUID, *, 
                                    start_datetime: Annotated[datetime, Body()], 
                                    end_datetime: Annotated[datetime, Body()],
                                    process_after: Annotated[timedelta, Body()],
                                    repeat_at: Annotated[Union[time, None], Body()]=None):
                start_process = start_datetime + process_after
                duration = end_datetime - start_process
                return {
                    "item_id": item_id,
                    "start_datetime": start_datetime,
                    "end_datetime": end_datetime,
                    "process_after": process_after,
                    "repeat_at": repeat_at,
                    "start_process": start_process,
                    "duration": duration
                }
