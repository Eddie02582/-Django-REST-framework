    function initialUserTable (){
      $('#user-table') .bootstrapTable({                        
          url: "/accounts/api/user/",
        showColumns : true,
        showColumnsToggleAll:true, //在欄位選擇開啟開關全部欄位
        showToggle : true, //名片式/table式切換
        showPaginationSwitch : true, //分頁/不分頁切換
        showRefresh : true, //重新整理
        showFullscreen: true,
        search : true, //查詢 
        pagination : true, 
        pageSize : 15,    
        height:500,
        buttons :"buttons",
        toolbar :"#toolbar",
        uniqueId :"id",
        columns: [ 
              {               
                title:'State',
                checkbox:true,                               
              },
              { 
                field :"id",
                title:'ID',
                visible:false, 
              },
              { 
                field :"username",
                title:'User Name',                             
              },
              { 
                field :"first_name", 
                title:'First Name',                                                    
              },      
              { 
                field :"last_name", 
                title:'Last Name',                                                    
              },      
              { 
                field :"email", 
                title:'Email',                                                    
              },   
              { 
                field :"profile.cell_phone_number", 
                title:'Cell Phone',                                                    
              }, 
              { 
                field :"profile.points", 
                title:'Points',                                                    
              },                 
          ],

        })                      

    }







