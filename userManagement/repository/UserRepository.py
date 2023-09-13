from userManagement.config.DataBaseConfig import DataBaseConfig, pymysql

class UserRepository:

    @staticmethod
    def saveUser(user = None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = f"""
            insert into user_tb
            values(0, %s, %s, %s, %s)
            """
            # 알아서 %s 자리에 넣어줌
            insertCount = cursor.execute(sql, (user.username, user.password, user.name, user.email))
            connection.commit()
            return insertCount
        except Exception as e :
            print()
            print(e)
            return 0

    @staticmethod
    def getUsersAll():
        try :
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            select
                user_id as userId,
                username,
                password,
                name,
                email
            from
                user_tb
            """
            cursor.execute(sql)
            rs = cursor.fetchall()
            return rs
        except Exception as e :
            print()
            print(e)
            return None

    @staticmethod
    def findByusername(username):
        try :
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
                select
                    user_id as userId,
                    username,
                    password,
                    name,
                    email
                from
                    user_tb
                where
                    username = %s
                """
            cursor.execute(sql,username)
            rs = cursor.fetchone()
            return rs
        except Exception as e :
            print()
            print(e)
            return None

    @staticmethod
    def deleteUser(username):
        try :
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor) # DictCursor로 사용하면 맵으로됨
            sql = """
            delete from user_tb
            where username = %s        
            """
            deleteCount = cursor.execute(sql,(username))
            connection.commit()
            return deleteCount
        except Exception as e :
            print()
            print(e)
            return 0

    @staticmethod
    def updateUser(user = None):
        try:
            connection = DataBaseConfig.getConnection()
            cursor = connection.cursor(pymysql.cursors.DictCursor)
            sql = """
            update user_tb
            set
                password = %s,
                name = %s,
                email = %s
            where
                user_id = %s
            """
            updateCount = cursor.execute(sql,
                         (user.get("password"), user.get("name"), user.get("email"), user.get("userId")))
            connection.commit()
            return updateCount
        except Exception as e :
            print(e)
            return 0