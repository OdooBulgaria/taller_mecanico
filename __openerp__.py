# -*- encoding: utf-8 -*-
 
{
    "name": "Taller Mecánico",
    "version": "1.0",
    "description": 
    """
        Agrega campos al pedido de ventas, adaptado a un taller mecánico
        Tiene dependencias que se descargan en
        
        bzr branch lp:sale-reports

        bzr branch lp:webkit-utils/7.0
    """,
    "author": "MAR Sistemas",
    "website": "http://www.marsistemas.com",
    "category": "Sales",
    "depends": ["base","sale","sale_stock","fleet","sale_order_webkit","purchase"],
    "data":['taller_mecanico_view.xml','taller_vehicle_view.xml','taller_shop_view.xml','security/taller_security.xml'],
    "demo_xml": [],
    "update_xml": [],
    "active": False,
    "installable": True,
    "certificate" : "",
}
