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
    def deleteUser(username):
        responseBody = bool(UserRepository.deleteUser(username))
        return ResponseEntity(body = responseBody)
