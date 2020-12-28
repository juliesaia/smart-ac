package com.example.juliesaia.accontrol;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;


import java.io.BufferedOutputStream;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.HashMap;
import java.util.Map;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.example.juliesaia.accontrol.CallAPI;
public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    }

    public void sendRequest(final View view){
        final RequestQueue queue = Volley.newRequestQueue(this);  // this = context
        String url = "http://SERVER_IP:SERVER_PORT";
        Response.ErrorListener response;

        final StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>()
                {
                    @Override
                    public void onResponse(String response) {
                        // response
                        Log.d("Response", response);
                    }
                },
                new Response.ErrorListener()
                {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // error

                    }
                }
        ) {
            @Override
            protected Map<String, String> getParams()
            {
                Map<String, String> params = new HashMap<String, String>();
                params.put("passwordstring", "on");
                EditText text = (EditText)findViewById(R.id.editText);
                String value = text.getText().toString();
                Integer inttemp = Math.toIntExact(Math.round((Integer.parseInt(value) - 32) * (.5556)));
                String temp = Integer.toString(inttemp);
                RadioGroup radioGroup = (RadioGroup) findViewById(R.id.fanradio);
                int selectedId = radioGroup.getCheckedRadioButtonId();
                RadioButton radioButton = (RadioButton) findViewById(selectedId);
                String fanlevel = radioButton.getText().toString();
                radioGroup = (RadioGroup) findViewById(R.id.vaneradio);
                selectedId = radioGroup.getCheckedRadioButtonId();
                radioButton = (RadioButton) findViewById(selectedId);
                String vanelevel = radioButton.getText().toString();
                params.put("temperature", temp);
                params.put("fanlevel", fanlevel);
                params.put("vanelevel", vanelevel);
                


                return params;
            }
        };
        queue.add(postRequest);
    }
    public void turnOff(View view) {
        RequestQueue queue = Volley.newRequestQueue(this);  // this = context
        String url = "http://SERVER_IP:SERVER_PORT";
        Response.ErrorListener response;

        StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>()
                {
                    @Override
                    public void onResponse(String response) {
                        // response
                        Log.d("Response", response);
                    }
                },
                new Response.ErrorListener()
                {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // error

                    }
                }
        ) {
            @Override
            protected Map<String, String> getParams()
            {
                Map<String, String> params = new HashMap<String, String>();
                params.put("passwordstring", "off");


                return params;
            }
        };
        queue.add(postRequest);
    }
}
