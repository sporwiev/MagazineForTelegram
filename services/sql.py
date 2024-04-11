from config import Config
from mysql import connector
from contextlib import closing

class DataBase:

    async def add_users(self,user_id,name):
        with closing(connector.connect(
            host='localhost',
            user='root',
            password='root'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                result = cursor.execute("""INSERT INTO users (`user_id`, `name`, `role`) VALUES (?, ?, ?)""",[user_id, name, 'admin' if user_id == Config.admin_ids else 'user'])
                connection.commit()
                return result


    # async def update_label(self, label, user_id):
    #     with self.connect:
    #         return self.cursor.execute("""UPDATE users SET label=(?) WHERE user_id=(?)""",
    #                                    [label, user_id])
    #
    # async def get_payment_status(self, user_id):
    #     with self.connect:
    #         return self.cursor.execute("""SELECT bought, label FROM users WHERE user_id=(?)""",
    #                                    [user_id]).fetchall()
    #
    # async def update_payment_status(self, user_id):
    #     with self.connect:
    #         return self.cursor.execute("""UPDATE users SET bought=(?) WHERE user_id=(?)""",
    #                                    [True, user_id])

    async def get_products(self,category_id):
        with closing(connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""SELECT * FROM products WHERE category_id={category_id} AND price > 0 AND count > 0""")
                result = cursor.fetchall()
                return result



    async def get_cart(self, user_id):
        with connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT * FROM cart WHERE user_id={user_id}""")
                result = cursor.fetchall()
                if(result == None):
                    return 'вы ничего не заказали'
                else:
                    return result

    async def add_to_cart(self, user_id, product_id):
        with connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"""INSERT INTO cart (user_id, product_id, count) VALUES ({user_id}, {product_id}, 1)""")
                result = cursor.fetchall()
                return result

    async def empty_cart(self, user_id):
        with connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        ) as connection:
            with connection.cursor() as cursor:
                return cursor.execute(f"""DELETE FROM cart WHERE user_id={user_id}""")

    async def get_categories(self):
        with closing(connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute("""SELECT * FROM categories""")
                #connection.commit()
                result = cursor.fetchall()

                return result
    async def update_category_id(self,category_id,name):
        with closing(connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""UPDATE `products` SET `category_id`='{category_id}' WHERE `name` = '{name}'""")
                connection.commit()
                return None
    async def get_acoproduct(self):
        with closing(connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute("""SELECT * FROM products""")
                #connection.commit()
                result = cursor.fetchall()

                return result
    async def del_items_product(self):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""TRUNCATE TABLE products;""")
                connection.commit()
                return None
    async def set_product(self, product_id,name,price,count,category_id):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO `products`(`product_id`, `name`, `price`, `count`, `category_id`) VALUES ('{product_id}','{name}','{price}','{count}','{category_id}')""")
                connection.commit()
                return None
    async def get_count(self, product_id):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""SELECT count FROM products WHERE product_id={product_id}""")
                result = cursor.fetchall()
                return result

    async def minus_plus(self, product_id, count, categoey_id):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""UPDATE `products` SET `count`='{str(count)}' WHERE product_id = {int(product_id)} AND category_id = {int(categoey_id)}""")
                connection.commit()
                return connection


    async def get_count_in_cart(self, user_id, product_id):
        with closing(connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""SELECT count FROM cart WHERE user_id={user_id} AND product_id={product_id}""")
                connection.commit()
                result = cursor.fetchall()
                return result

    async def get_count_in_stock(self, product_id):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""SELECT count FROM products WHERE product_id={product_id}""")
                connection.commit()
                result = cursor.fetchall()
                return result
    async def get_product_id_n(self):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""SELECT product_id FROM products ORDER BY id DESC LIMIT 1""")
                result = cursor.fetchall()
                return result
    async def create_tableSum(self,magasin_user):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""CREATE TABLE `magasin{magasin_user}` ( `id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(255) NOT NULL , `price` INT(10) NOT NULL , `category_id` INT(2) NOT NULL , `product_id` INT(10) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;""")
                connection.commit()
                return None
    async def drop_tableSum(self,magasin_user):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""DROP TABLE `magasin{magasin_user}`""")
                connection.commit()
                return None
    async def drop_tableSpis(self,magasin_user):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""DROP TABLE `spis{magasin_user}`""")
                connection.commit()
                return None
    async def create_tableSpis(self,spis_user):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""CREATE TABLE `spis{spis_user}` ( `id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(255) NOT NULL , `price` INT(10) NOT NULL , `category_id` INT(2) NOT NULL , `product_id` INT(10) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;""")
                connection.commit()
                return None

    async def set_spis(self,spis_user,name,price,product_id,category_id):
        nasvanie = f'spis{spis_user}'
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""INSERT INTO {nasvanie} (`product_id`, `name`, `price`, `category_id`) VALUES ('{product_id}','{str(name)}','{int(price)}','{int(category_id)}')""")
                connection.commit()
                return None

    async def get_id(self):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT id FROM products""")
                result = cursor.fetchall()
                return result
    async def get_product_id(self):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT product_id FROM products""")
                result = cursor.fetchall()
                return result
    async def get_price(self):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT price FROM products""")
                result = cursor.fetchall()
                return result
    async def get_county(self):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT count FROM products """)
                result = cursor.fetchall()
                return result
    async def get_category_id(self):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT category_id FROM products""")
                result = cursor.fetchall()
                return result
    async def get_names(self):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT name FROM products""")
                result = cursor.fetchall()
                return result
    async def get_name(self,product_id):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT name FROM products WHERE product_id = {int(product_id)}""")
                result = cursor.fetchall()
                return result
    async def get_magasin_accout_price(self,magasin_user):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT price FROM `magasin{magasin_user}`;""")
                result = cursor.fetchall()
                return result
    async def get_spis_accout_price(self,spis_user):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT price FROM `spis{spis_user}`;""")
                result = cursor.fetchall()
                return result
    async def get_magasin_accout_name(self,magasin_user):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT name FROM magasin{magasin_user};""")
                result = cursor.fetchall()
                return result
    async def get_spis_accout_name(self,spis_user):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT name FROM spis{spis_user};""")
                result = cursor.fetchall()
                return result
    async def del_price_magasin(self,magasin_user,name,price,product_id,category_id):
        nasvanie = f'magasin{magasin_user}'
        print(nasvanie)
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""INSERT INTO {nasvanie} (`product_id`, `name`, `price`, `category_id`) VALUES ('{product_id}','{str(name)}','{int(price)}','{int(category_id)}')""")
                connection.commit()
                return None
    async def set_magasin(self,magasin_user,name,price,product_id,category_id):
        nasvanie = f'magasin{magasin_user}'
        print(nasvanie)
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""INSERT INTO {nasvanie} (`product_id`, `name`, `price`, `category_id`) VALUES ('{product_id}','{str(name)}','{int(price)}','{int(category_id)}')""")
                connection.commit()
                return None
    async def get_price_product(self,product_id,category_id):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(
                    f"""SELECT price FROM products WHERE product_id = {product_id} AND category_id = {category_id}""")

                result = cursor.fetchall()
                return result

    async def insert_product_in_mymagasin(self,message,product_id,name,price,category_id):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO `magasin{message}`(`product_id`, `name`, `price`, `category_id`) VALUES ({product_id},{name},{price},{category_id})""")
                connection.commit()
                result = cursor.fetchall()
                return result

    async def insert_product(self,product_id,name,price,count,category_id):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""INSERT INTO `products`(`product_id`, `name`, `price`, `count`, `category_id`) VALUES ({product_id},{name},{price},{count},{category_id})""")
                connection.commit()
                result = cursor.fetchall()
                return result

    async def remove_one_item(self, product_id, user_id):
        with connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        ) as connection:
            with connection.cursor() as cursor:
                return cursor.execute(f"""DELETE FROM cart WHERE product_id={product_id} AND user_id={user_id}""")

    async def change_count(self, count, product_id, user_id):
        with connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        ) as connection:
            with connection.cursor() as cursor:
                return cursor.execute(f"""UPDATE cart SET count={count} WHERE product_id={product_id} AND user_id={user_id}""")
    async def del_product(self,product_id):
        with closing(connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='telegram_bot_db'
        )) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(f"""DELETE FROM `products` WHERE product_id = {product_id}""")
                connection.commit()
                return None

