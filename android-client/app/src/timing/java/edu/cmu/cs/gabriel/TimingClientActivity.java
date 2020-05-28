package edu.cmu.cs.gabriel;

import android.Manifest;
import android.content.Context;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationManager;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Build;
import android.os.StrictMode;

import androidx.annotation.RequiresApi;
import androidx.core.app.ActivityCompat;


import java.util.List;

import edu.cmu.cs.gabriel.client.comm.LocationHelper;

import edu.cmu.cs.gabriel.network.TimingComm;

import static edu.cmu.cs.gabriel.client.Util.ValidateEndpoint;

public class TimingClientActivity extends GabrielClientActivity {
    private TimingComm timingComm;

    @RequiresApi(api = Build.VERSION_CODES.M)
    @Override
    void setupComm() {
        String serverURL = ValidateEndpoint(this.serverIP, Const.PORT);

        // Get info to capture in the log
        // Think this should be in new class

        // This may be a bad idea -- had to do to get influxdb to work.
        if (android.os.Build.VERSION.SDK_INT > 9)
        {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }

        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            requestPermissions(new String[]{Manifest.permission.ACCESS_COARSE_LOCATION}, 0);
            return;
        }
        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            requestPermissions(new String[] {Manifest.permission.ACCESS_FINE_LOCATION}, 0);
            return;
        }
//        if (ActivityCompat.checkSelfPermission(this, Manifest.permission.READ_PHONE_STATE) != PackageManager.PERMISSION_GRANTED) {
//            requestPermissions(new String[] {Manifest.permission.READ_PHONE_STATE}, 0);
//            return;
//        }
//        TelephonyManager teleMan = (TelephonyManager) this.getSystemService(Context.TELEPHONY_SERVICE);
//
//        List<CellInfo> cellInfo = teleMan.getAllCellInfo();
//
//        SubscriptionManager subMan = (SubscriptionManager) this.getSystemService(Context.TELEPHONY_SUBSCRIPTION_SERVICE);
//        List<SubscriptionInfo> subInfo = subMan.getActiveSubscriptionInfoList();
        ConnectivityManager conMan = (ConnectivityManager) this.getSystemService(Context.CONNECTIVITY_SERVICE);


        LocationManager locMan = (LocationManager) this.getSystemService(Context.LOCATION_SERVICE);
        LocationHelper locHelper = new LocationHelper();
        locMan.requestLocationUpdates("gps",1000, (float) 1, locHelper);
        List<String> locProviders = locMan.getAllProviders();
        Location locationGPS = locMan.getLastKnownLocation(LocationManager.GPS_PROVIDER);
//        Location locationNet = locMan.getLastKnownLocation(LocationManager.NETWORK_PROVIDER);



        this.timingComm = new TimingComm(serverURL, conMan, locMan,this, this.returnMsgHandler,
                Const.TOKEN_LIMIT);
         this.comm = this.timingComm;
    }

    @Override
    protected void onPause() {
        this.timingComm.logAvgRtt();
        super.onPause();
    }
}
