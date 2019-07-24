/**
 * Created by sharifulislam on 5/29/16.
 */
/**
 * General Ledger
 */
    $(document).ready(function () {
        $('#timechange').change(function () {
            if($(this).val() == 'y'){
                $("#range").html("Select Year : <select class='form-control' style='width:100%'><option value='2015'>2015</option><option value='2016'>2016</option><option value='2017'>2017</option><option value='2018'>2018</option><option value='2019'>2019</option><option value='2019'>2019</option><option value='2019'>2019</option><option value='2020'>2020</option><option value='2021'>2021</option><option value='2022'>2022</option><option value='2023'>2023</option><option value='2024'>2024</option></select>");

            }else if($(this).val() == 'q'){
                $("#range").html("Select Quarter: <select class='form-control' style='width:100%'><option value='1'>Jan -Mar</option><option value='2'>Apr - Jun</option><option value='3'>Jul -Sep</option><option value='4'>Oct - Dec</option>");
            }else if($(this).val() == 'm'){
                $("#range").html("Select Month : <select class='form-control' style='width:100%'><option value='1'>January</option><option value='2'>Feburary</option><option value='3'>March</option><option value='4'>April</option><option value='5'>May</option><option value='6'>June</option><option value='7'>July</option><option value='8'>August</option><option value='9'>September</option><option value='10'>October</option><option value='11'>November</option><option value='12'>December</option></select>");
            }else if($(this).val() == 'd'){
                $("#range").html("Start Date : <input type='text' name='startyr' class='reservationtime form-control' style='width:100%'>End Date : <input type='text' name='endyr' class='reservationtime form-control' style='width:100%'>");
                $('.reservationtime').daterangepicker({
                    singleDatePicker: true, //<==HERE
                });
            }else{
                $("#range").text("Select a Option")
            }
        });
    });