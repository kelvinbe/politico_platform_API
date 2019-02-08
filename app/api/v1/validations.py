
def validate_party(data, is_patch=False):
    party_fields = ("name", "hqAddress", "logoUrl")
    message = ""
    if is_patch:
        try:
            name = data["name"]
        except KeyError:
            message = "name is required"
        else:
            if not isinstance(name, (str, bytes)):
                message = "name must be a string"
            else:
                if not name.strip():
                    message = "name cannot be empty"
    else:
        if not set(data.keys()) == set(party_fields):
            message = "Party Fields are name, hqAddress, logoUrl"
        else:
            name = data["name"]
            hqAddress = data["hqAddress"]
            logoUrl = data["logoUrl"]
            if not isinstance(name, (str, bytes)):
                message = "name must be a string"
            elif not isinstance(hqAddress, (str, bytes)):
                message = "hqAddress must be a string"
            elif not isinstance(logoUrl, (str, bytes)):
                message = "logoUrl must be a string"
            else:

                if not name.strip():
                    message = "name cannot be empty"
                if not hqAddress.strip():
                    message = "hqAddress cannot be empty"
                if not logoUrl.strip():
                    message = "logoUrl cannot be empty"
    return message


def validate_office(data):
    office_fields = ("name", "type")
    message = ""
    if not set(data.keys()) == set(office_fields):
            message = "Office Fields are name and type"
    else:
            name = data["name"]
            type = data["type"]
            if not isinstance(name, (str, bytes)):
                message = "name must be a string"
            elif not isinstance(type, (str, bytes)):
                message = "type must be a string"
            else:

                if not name.strip():
                    message = "name cannot be empty"
                if not type.strip():
                    message = "type cannot be empty"
    return message










