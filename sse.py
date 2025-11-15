from typing import Any, Optional
import json


def message(data: Any, event: Optional[str] = None, id_: Optional[str] = None, retry: Optional[int] = None) -> str:
    if not isinstance(data, str):
        data = json.dumps(data)

    lines = [f'data:{line}' for line in data.splitlines()]

    if event:
        lines.insert(0, f'event:{event}')

    if id_:
        lines.append(f'id:{id_}')

    if retry:
        lines.append(f'retry:{retry}')

    return '\n'.join(lines) + '\n\n'
