import os
import django
import csv
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "class404.settings")
django.setup()

from product.models import(
        Brand,
        Category,
        Gender,
        ClassLevel,
        Age,
        Product,
        ProductAge,
        ProductUserlike, Review,
        )

from user.models     import UserTier, UserType, User
from order.models    import OrderStatus, Address, Order

## brand 파일 업데이트
CSV_PATH = "./csv/brand.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            brand_id = row[0]
            name     = row[1]
            print(brand_id, name)

            Brand.objects.create(name = name)

## Category 파일 업데이트
CSV_PATH = "./csv/category.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            category_id = row[0]
            name        = row[1]
            brand_id    = row[2]
            print(category_id, name, brand_id)

            brand = Brand.objects.get(id=brand_id)

            Category.objects.create(
                    name = name,
                    brand_id = brand.id
                    )
#
## age 파일 업데이트
CSV_PATH = "./csv/age.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            age_id = row[0]
            group  = row[1]

            print(age_id, group)

            Age.objects.create(group=group)

## UserLevel 업데이트
##CSV_PATH = "./csv/level.csv"
##with open(CSV_PATH) as in_file:
##    data_reader = csv.reader(in_file)
##    next(data_reader, None)
##    for row in data_reader:
##        if row[0]:
##            user_level_id = row[0]
##            name          = row[1]
#
#            print(user_level_id, name)

#           UserLevel.objects.create(name = name)


## UserTier 업데이트
CSV_PATH = "./csv/user_tier.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            user_tier_id = row[0]
            name          = row[1]

            print(user_tier_id, name)

            UserTier.objects.create(name = name)


## order_status 업데이트
CSV_PATH = "./csv/order_status.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            order_status_id = row[0]
            name            = row[1]

            print(order_status_id, name)

            OrderStatus.objects.create(name=name)

## usertype 업데이트
CSV_PATH = "./csv/user_type.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            user_type_id = row[0]
            name         = row[1]
            print(user_type_id, name)

            UserType.objects.create(name=name)


## user 업데이트
CSV_PATH = "./csv/user.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            user_id      = row[0]
            name         = row[1]
            email        = row[2]
            password     = row[3]
            image_url    = row[4]
            social_login = row[5]
            tier_id      = row[6]
            user_type_id = row[7]
            print(user_id, name, email, password, image_url, social_login, tier_id, user_type_id)

            tier      = UserTier.objects.get(id=tier_id)
            user_type = UserType.objects.get(id=user_type_id)

            User.objects.create(
                    name         = name,
                    email        = email,
                    password     = password,
                    image_url    = image_url,
                    social_login = social_login,
                    tier_id      = tier.id,
                    user_type_id = user_type.id)


## class_level 업데이트
CSV_PATH = "./csv/class_level.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            class_level_id = row[0]
            name           = row[1]
            print(class_level_id, name)

            ClassLevel.objects.create(name=name)



## product 업데이트
CSV_PATH = "./csv/product.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            product_id      = row[0]
            title           = row[1]
            price           = row[2]
            gift            = row[3]
            available_now   = row[4]
            introduction    = row[5]
            thumbnail_url   = row[6]
            category_id     = row[7]
            satisfaction    = row[8]
            user_id         = row[9]
            class_level_id  = row[10]
            age_id          = row[11]
            description     = row[12]

            print(product_id, title, price, gift, available_now, introduction, thumbnail_url, category_id, class_level_id,age_id, description)

            category    = Category.objects.get(id=category_id)
            class_level = ClassLevel.objects.get(id=class_level_id)
            user        = User.objects.get(id=user_id)

            Product.objects.create(
                    title            = title, 
                    price            = price,
                    gift             = gift,
                    available_now    = available_now,
                    introduction     = introduction,
                    thumbnail_url    = thumbnail_url,
                    category_id      = category.id,
                    satisfaction     = satisfaction,     
                    user             = user,
                    class_level_id   = class_level.id,
                    description      = description)
            
            product = Product.objects.get(id=product_id)


            if Age.objects.filter(id=age_id).first() != None:
                age = Age.objects.filter(id=age_id).first()
                product.age.add(age)

# reviews 업데이트
CSV_PATH = "./csv/reviews.csv"
with open(CSV_PATH) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        if row[0]:
            review_id     = row[0]
            image_url     = row[1]
            description   = row[2]
            user_id       = row[3]
            product_id    = row[4]
            print(review_id, image_url, description ,user_id, product_id)

            user = User.objects.get(id=user_id)
            product = Product.objects.get(id=product_id)

            Review.objects.create(
                    image_url   = image_url,
                    description = description,
                    product_id  = product.id,
                    user_id     = user.id
                    )
           






