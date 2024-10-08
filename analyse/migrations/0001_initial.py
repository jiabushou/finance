# Generated by Django 5.0.4 on 2024-05-03 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OperateRecord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ctime', models.DateTimeField(db_comment='创建时间')),
                ('mtime', models.DateTimeField(db_comment='修改时间')),
                ('bargain_time', models.DateTimeField(db_comment='成交时间')),
                ('bond_code', models.CharField(db_comment='证劵代码', max_length=10)),
                ('bond_name', models.CharField(db_comment='证劵名称', max_length=10)),
                ('operate_kind', models.CharField(db_comment='操作类型(in:买入;out:卖出)', max_length=10)),
                ('bargain_number', models.IntegerField(db_comment='成交数量(100的整数倍)')),
                ('bargain_unit_price', models.DecimalField(db_comment='成交均价', decimal_places=3, max_digits=10)),
                ('bargain_amount', models.DecimalField(db_comment='成交金额', decimal_places=3, max_digits=10)),
                ('contract_no', models.CharField(db_comment='合同编号', max_length=20)),
                ('bargain_no', models.CharField(db_comment='成交编号', max_length=20, unique=True)),
                ('fee', models.DecimalField(db_comment='手续费', decimal_places=3, max_digits=10)),
                ('stamp_duty', models.DecimalField(db_comment='印花税', decimal_places=3, max_digits=10)),
                ('other_fee', models.DecimalField(db_comment='其它杂费', decimal_places=3, max_digits=10)),
                ('happen_amount', models.DecimalField(db_comment='发生金额', decimal_places=3, max_digits=10)),
                ('left_amount', models.DecimalField(db_comment='资金余额', decimal_places=3, max_digits=10)),
                ('trade_market', models.CharField(db_comment='交易市场', max_length=10)),
                ('share_holder_account', models.CharField(db_comment='股东账户', max_length=10)),
                ('delivery_date', models.DateTimeField(db_comment='交收日期')),
                ('bond_full_name', models.CharField(db_comment='证劵中文全称', max_length=10)),
            ],
            options={
                'db_table': 'operate_record',
                'managed': False,
            },
        ),
    ]
