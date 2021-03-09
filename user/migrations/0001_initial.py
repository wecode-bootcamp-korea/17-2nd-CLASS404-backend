from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user_tiers',
            },
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'user_types',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=500, unique=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image_url', models.URLField(default='https://media.vlpt.us/images/c_hyun403/post/7b35d3bb-44be-41bf-8192-0ccc426b465c/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-02-26%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2012.53.02.png', max_length=2000)),
                ('social_login', models.CharField(max_length=50, null=True)),
                ('tier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertier')),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.usertype')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='CreatorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'creator_info',
            },
        ),
    ]
