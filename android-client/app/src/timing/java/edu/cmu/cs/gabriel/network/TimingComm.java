package edu.cmu.cs.gabriel.network;

import android.app.Activity;
import android.location.LocationManager;
import android.net.ConnectivityManager;
import android.os.Build;
import android.os.Handler;

import androidx.annotation.RequiresApi;

import edu.cmu.cs.gabriel.client.comm.TimingServerComm;

public class TimingComm extends BaseComm {
    TimingServerComm timingServerComm;

    @RequiresApi(api = Build.VERSION_CODES.O)
    public TimingComm(String serverURL, ConnectivityManager conMan, LocationManager locMan, final Activity activity,
                      final Handler returnMsgHandler, String tokenLimit) {
        super(activity, returnMsgHandler);

        if (tokenLimit.equals("None")) {
            this.timingServerComm = new TimingServerComm(this.consumer, this.onDisconnect,
                    serverURL, conMan, locMan, activity.getApplication());
        } else {
            this.timingServerComm = new TimingServerComm(this.consumer, this.onDisconnect,
                    serverURL, conMan, locMan, activity.getApplication(), Integer.parseInt(tokenLimit));
        }

        this.serverCommCore = timingServerComm;
    }

    public void logAvgRtt() {
        this.timingServerComm.logAvgRtt();
    }
}
