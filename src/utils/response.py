class Response:
    def success(self, message, info=None):
        message_formated = message.format(info)
        res = {"Message": message_formated}
        return res

    def failed(self, message, error=None):
        message_formated = message.format(error)
        res = {"Error": message_formated}
        return res
