from userManagement.util.ResponseUtil import ResponseEntity
from userManagement.repository.UserRepository import UserRepository

class UserController:

    @staticmethod
    def registerUser(user = None):
        responseBody = bool(UserRepository.saveUser(user))
        return ResponseEntity(body = responseBody)

    @staticmethod
    def getUsersALl():
        responseBody = UserRepository.getUsersAll()
        return ResponseEntity(body = responseBody)

    @staticmethod
    def getUser(username):
        responseBody = UserRepository.findByusername(username)
        return ResponseEntity(body = responseBody)

    @staticmethod
    def deleteUser(userId):
        responseBody = bool(UserRepository.deleteUser(userId))
        return ResponseEntity(body = responseBody)

    @staticmethod
    def updateUser(user = None):
        responseBody = UserRepository.updateUser(user)
        return ResponseEntity(body = responseBody)